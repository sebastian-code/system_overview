#! /usr/bin/python3
# -*- coding:utf-8 -*-

import subprocess


class InformeLinux(object):
    """docstring de la clase InformeLinux, clase creada con la finalidad de
    aprovechar al maximo las interacciones con cualquier sistema Linux
    (exclusivamente).

    Los diferentes metodos de la clase interactuan con las herramientas de
    cualquier sistema Linux estandar, permitiendole extraer y proveer la mayor
    cantidad de informacion posible sobre el sistema en que se trabaja,
    ahorrando los esfuerzos ingentes que se necesitan para ese mismo proceso
    haciendo uso de las mismas herramientas.

    Aunque Python cuenta con algunas de las funcionalidades, y quizas sea
    valido implementarlas, parte del ejercicio es no necesitar implementar nada
    adicional."""
    def __init__(self):
        super(InformeLinux, self).__init__()

    # cat /proc/cpuinfo | grep 'model name' | head -n 1 | sed 's/model name.*: //g'
    def nom_proc():
        """Metodo que retorna el nombre del procesador del equipo, pero es
        necesario tener en cuenta que en los casos que por arquitectura el
        equipo analizado tenga diferentes procesadores, este asumira unicamente
        la primera coincidencia en el archivo cpuinfo en la carpeta proc."""
        p1 = subprocess.Popen(['cat', '/proc/cpuinfo'], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['grep', 'model name'], stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p3 = subprocess.Popen(['head', '-n 1'], stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p4 = subprocess.Popen(['sed', 's/model name.*: //g'], stdin=p3.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p2.stdout.close()
        p3.stdout.close()
        return str(p4.communicate()[0])[2:-3]

    # cat /proc/cpuinfo | grep 'cpu MHz' | head -n 1 | sed 's/cpu MHz.*: //g'
    def vel_proc():
        p1 = subprocess.Popen(['cat', '/proc/cpuinfo'], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['grep', 'cpu MHz'], stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p3 = subprocess.Popen(['head', '-n 1'], stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p4 = subprocess.Popen(['sed', 's/cpu MHz.*: //g'], stdin=p3.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p2.stdout.close()
        p3.stdout.close()
        return str(p4.communicate()[0])[2:-3]

    # cat /proc/cpuinfo | grep 'cpu cores' | head -n 1 | sed 's/cpu MHz.*: //g'
    def num_nucleos():
        p1 = subprocess.Popen(['cat', '/proc/cpuinfo'], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['grep', 'cpu cores'], stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p3 = subprocess.Popen(['head', '-n 1'], stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p4 = subprocess.Popen(['sed', 's/cpu cores.*: //g'], stdin=p3.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()
        p2.stdout.close()
        p3.stdout.close()
        return str(p4.communicate()[0])[2:-3]

    # lspci | grep VGA | sed 's/.*VGA compatible controller://g'
    def vga_modelo():
        p1 = subprocess.Popen('lspci', stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['grep', 'VGA'], stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p3 = subprocess.Popen(['sed', 's/.*VGA compatible controller://g'],
                              stdin=p2.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        p2.stdout.close()
        return str(p3.communicate()[0])[3:-12]

    # lsmod | grep 'fglrx | nvidia | i915 | i965 | intel_agp | r200 | r300 | r600 | swrast | svga | radeon | noveau'
    def vga_driver():
        p1 = subprocess.Popen('lsmod', stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['grep', 'fglrx\\|nvidia\\|i915\\|i965\\|intel_agp\\|r200\\|r300\\|r600\\|swrast\\|svga\\|radeon\\|noveau'],
                              stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        st = str(p2.communicate()[0])[2:-3].replace('\\n', '<br />')
        return st

    # glxinfo 2>&1 | grep -i 'direct rendering'
    def vga_rendering():
        p1 = subprocess.Popen(['glxinfo'], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['grep', '-i', 'direct rendering'],
                              stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        return str(p2.communicate()[0])[2:-3]

    # xrandr
    def vga_displays():
        p1 = subprocess.Popen('xrandr', stdout=subprocess.PIPE)
        st = str(p1.communicate()[0])[2:-3].replace('\\n', '<br />')
        return st

    # lspci | grep Audio | sed 's/.*Audio device://g'
    def snd_modelo():
        p1 = subprocess.Popen('lspci', stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['grep', 'Audio'], stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p3 = subprocess.Popen(['sed', 's/.*Audio device://g'],
                              stdin=p2.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        p2.stdout.close()
        return str(p3.communicate()[0])[3:-3]

    # lsmod | grep 'snd'
    def snd_driver():
        p1 = subprocess.Popen('lsmod', stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['grep', 'snd'],
                              stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        st = str(p2.communicate()[0])[2:-3].replace('\\n', '<br />')
        return st

    # grep MemTotal /proc/meminfo | sed 's/MemTotal: //g'
    def mem_total(arg):
        p1 = subprocess.Popen(['grep', 'MemTotal', '/proc/meminfo'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['sed', 's/MemTotal: //g'],
                              stdin=p1.stdout, stdout=subprocess.PIPE)
        return str(p2.communicate()[0])[2:-3]

    # grep MemFree /proc/meminfo | sed 's/MemFree: //g'
    def mem_libre(arg):
        p1 = subprocess.Popen(['grep', 'MemFree', '/proc/meminfo'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['sed', 's/MemFree: //g'],
                              stdin=p1.stdout, stdout=subprocess.PIPE)
        return str(p2.communicate()[0])[2:-3]

    # grep SwapTotal /proc/meminfo | sed 's/SwapTotal: //g'
    def swap_total(arg):
        p1 = subprocess.Popen(['grep', 'SwapTotal', '/proc/meminfo'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['sed', 's/SwapTotal: //g'],
                              stdin=p1.stdout, stdout=subprocess.PIPE)
        return str(p2.communicate()[0])[2:-3]

    # grep SwapFree /proc/meminfo | sed 's/SwapFree: //g'
    def swap_libre(arg):
        p1 = subprocess.Popen(['grep', 'SwapFree', '/proc/meminfo'],
                              stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['sed', 's/SwapFree: //g'],
                              stdin=p1.stdout, stdout=subprocess.PIPE)
        return str(p2.communicate()[0])[2:-3]

    # df -h
    def particionado():
        p1 = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
        st = str(p1.communicate()[0])[2:-3].replace('\\n', '<br />')
        return st

    # ifconfig
    def redes():
        p1 = subprocess.Popen('ifconfig', stdout=subprocess.PIPE)
        st = str(p1.communicate()[0])[2:-3].replace('\\n', '<br />')
        return st

    # cat /etc/apt/sources.list
    def sw_sources():
        p1 = subprocess.Popen(['cat', '/etc/apt/sources.list'],
                              stdout=subprocess.PIPE)
        st = str(p1.communicate()[0])[2:-3].replace('\\n', '<br />')
        return st

    # dpkg-query --show | sed 's/\n/<\/br>/g'
    def sw_instalado():
        p1 = subprocess.Popen(['dpkg-query', '--show'], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['sed', 's/\\n/<\/br>/g'],
                              stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        st = str(p2.communicate()[0])[2:-3].replace('\\n', '<br />')
        return st

    # lsmod
    def kernel():
        p1 = subprocess.Popen('lsmod', stdout=subprocess.PIPE)
        st = str(p1.communicate()[0])[2:-3].replace('\\n', '<br />')
        return st
