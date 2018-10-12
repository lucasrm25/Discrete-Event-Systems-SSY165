import os
import platform
import subprocess

from IPython.display import Image

SYSTEM = platform.system()


def plot_automaton(automaton, file_name_no_extension):
    tmp_file = 'util\\tmp_aut.dot'
    with open(tmp_file, 'w') as tmp:
        tmp.write('digraph G {\n')

        for state in automaton.forbidden:
            tmp.write('\t"{}" [shape=box, color=red];\n'.format(state))

        for state in automaton.marked - automaton.forbidden:
            tmp.write('\t"{}" [shape=ellipse];\n'.format(state))

        for state in automaton.states - (automaton.marked | automaton.forbidden):
            tmp.write('\t"{}" [shape=plaintext];\n'.format(state))

        for transition in automaton.trans:
            tmp.write('\t"{}" -> "{}" [label="{}"];\n'.format(transition.source, transition.target, transition.event))

        tmp.write('\tinit [shape=plaintext, label=""];\n')
        tmp.write('\tinit -> "{}";\n'.format(automaton.init))

        tmp.write('}')

    pic = create_image(tmp_file, file_name_no_extension)
    os.remove(tmp_file)
    return pic


def plot_petrinet(petrinet, file_name_no_extension):
    tmp_file = 'util\\tmp_net.dot'
    with open(tmp_file, 'w') as tmp:
        tmp.write('digraph G {\n')

        for place in petrinet.places:
            tokens = '&#9679;' * place.marking + '\\n'
            tmp.write('\t"{}" [shape=circle, label="{}"];\n'.format(place.label, tokens + place.label))

        for trans in petrinet.transitions:
            tmp.write(
                '\t"{}" [shape=rectangle, style=filled, fillcolor=grey, fixedsize=true, height=0.2, width=0.6, label="{}"];\n'.format(
                    trans, trans))

        for arc in petrinet.arcs:
            tmp.write(
                '\t"{}" -> "{}" [label="  {}"];\n'.format(arc.source, arc.target, arc.weight if arc.weight > 1 else ""))

        tmp.write('}')

    pic = create_image(tmp_file, file_name_no_extension)
    os.remove(tmp_file)
    return pic


def plot_digraph(digraph, file_name_no_extension):
    tmp_file = 'util\\tmp_graph.dot'
    with open(tmp_file, 'w') as tmp:
        tmp.write('digraph G {\n')

        tmp.write('\t"{}" [shape=box];\n'.format(digraph.init))

        for node in digraph.nodes - {digraph.init}:
            tmp.write('\t"{}" [shape=plaintext];\n'.format(node))

        for edge in digraph.edges:
            tmp.write('\t"{}" -> "{}" [label="  {}"];\n'.format(edge.source, edge.target, edge.label))

        tmp.write('}')

    pic = create_image(tmp_file, file_name_no_extension)
    os.remove(tmp_file)
    return pic


def create_image(dot_file, image_name):
    if SYSTEM == 'Windows':
        exe = 'util\\dot'
    else:
        try:
            subprocess.run(['dot', '-V'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
        except Exception as e:
            if SYSTEM == 'Darwin':
                raise OSError('It seems your version of MacOS does not have Graphviz installed!\n'
                              'You have 3 options now:\n'
                              '\t-Follow the instructions on http://graphviz.org/download/\n'
                              '\t-Get https://www.anaconda.com/download/#macos and try "$ conda install graphviz"\n'
                              '\t-Use another computer running Windows or Linux')
            else:
                raise OSError('Graphviz not found! Try: $ sudo apt install graphviz')
        else:
            exe = 'dot'

    try:
        subprocess.run([exe, '-Tpng', dot_file, '-o{}.png'.format(image_name)], stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, check=True)
    except subprocess.CalledProcessError as e:
        raise ChildProcessError(e.stdout)

    return Image('{}.png'.format(image_name))
