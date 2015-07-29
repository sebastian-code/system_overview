#! /usr/bin/python3
# -*- coding:utf-8 -*-

import platform
import os
import subprocess


# cat /proc/cpuinfo | grep 'model name' | head -n 1 | sed 's/model name.*: //g'
def nom_proc():
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
def mem_query(arg):
    p1 = subprocess.Popen(['grep', '{}'.format(arg), '/proc/meminfo'],
                          stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['sed', 's/{}: //g'.format(arg)], stdin=p1.stdout,
                          stdout=subprocess.PIPE)
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


def reporte(arg):
    archivo_reporte.write(arg)


def header():
    reporte('''<!DOCTYPE HTML>
<html>
    <head>
        <title>Reporte del Sistema Local Linux</title>
        <style>
            tr > td:first-child { font-weight:bold; }
        </style>
    </head>
    <body>''')
    reporte('''
        <h2>Nombre del usuario e identificador de red</h2>
        <h2>{}@{}</h2>'''.format(os.getlogin(), platform.node()))


def linea_tabla(arg1, arg2):
    reporte('''
        <tr><td>{0}</td><td>{1}</td></tr>'''.format(arg1, arg2))


def footer():
    reporte('''
    </body>
</html>
    ''')


def informacion_basica():
    reporte('''
        <h3>Informacion general del Sistema</h3>
        <table border=0>''')
    linea_tabla('Nombre del Host:', platform.node())
    linea_tabla('Distribucion:', (platform.linux_distribution()[0],
                                  platform.linux_distribution()[1]))
    linea_tabla('Kernel:', platform.release())
    linea_tabla('Arquitectura:', platform.machine())
    reporte('</table>')


def informacion_cpu():
    reporte('''
        <h3>Configuracion de Hardware</h3>
        <h4>Procesador</h4>
        <table border=0>''')
    linea_tabla('Nombre del Procesador:', nom_proc())
    linea_tabla('Velocidad del Procesador:', vel_proc())
    linea_tabla('Numero de Nucleos:', num_nucleos())
    linea_tabla('Procesos en Paralelo:', os.cpu_count())
    reporte('</table>')


def informacion_graph():
    reporte('''
        <h4>Graficos</h4>
        <table border=0>
    ''')
    linea_tabla('Modelo:', vga_modelo())
    linea_tabla('Driver:', '''<pre>{}</pre>'''.format(vga_driver()))
    linea_tabla('Rendering:', vga_rendering())
    linea_tabla('Displays:', '<pre>{}</pre>'.format(vga_displays()))
    reporte('</table>')


def informacion_snd():
    reporte('''
        <h4>Sonidos</h4>
        <table border=0
    ''')
    linea_tabla('Modelo:', snd_modelo())
    linea_tabla('Driver:', '<pre>{}</pre>'.format(snd_driver()))
    reporte('</table>')


def informacion_mem():
    reporte('''
        <h4>Memoria</h4>
        <table border=0>
    ''')
    linea_tabla('RAM Total:', mem_query('MemTotal'))
    linea_tabla('RAM Libre:', mem_query('MemFree'))
    linea_tabla('Swap Total:', mem_query('SwapTotal'))
    linea_tabla('Swap Libre:', mem_query('SwapFree'))
    reporte('</table>')


def informacion_part():
    reporte('''
        <h4>Particiones</h4>
        <table border=0>
    ''')
    linea_tabla('', '<pre>{}</pre>'.format(particionado()))
    reporte('</table>')


def informacion_redes():
    reporte('''
        <h4>Interfaces de Red</h4>
        <table border=0>
    ''')
    linea_tabla('', '<pre>{}</pre>'.format(redes()))
    reporte('</table>')


def informacion_sw():
    reporte('''
        <h3>Informacion del Software</h3>
        <h4>Fuentes del Software</h4>
        <table border=0>''')
    linea_tabla('', '<pre>{}</pre>'.format(sw_sources()))
    reporte('</table>')
    reporte('''
        <h4>Software Instalado</h4>
        <table border=0>''')
    linea_tabla('', '<pre>{}</pre>'.format(sw_instalado()))
    reporte('</table>')


def informacion_kernel():
    reporte('''
        <h3>Informacion del Kernel</h3>
        <h4>Resumen de Modulos del Kernel</h4>
        <table border=0>''')
    linea_tabla('', '<pre>{}</pre>'.format(kernel()))
    reporte('</table>')

import time

if __name__ == '__main__':
    os.chdir(os.path.expanduser('~'))
    fecha = time.strftime('%Y-%m-%d_') + time.strftime('%H-%M-%S')
    archivo_reporte = open('sys_report_{}.html'.format(fecha), 'a+')
    header()
    informacion_basica()
    informacion_cpu()
    informacion_graph()
    informacion_snd()
    informacion_mem()
    informacion_part()
    informacion_redes()
    informacion_sw()
    informacion_kernel()
    footer()
    archivo_reporte.close()
