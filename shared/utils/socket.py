import socket
import platform
import struct


def _set_keepalive_linux(
        sock: socket.socket,
        keep_alive_time: int = 1,
        keep_alive_interval: int = 3,
        max_probes: int = 5
):

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, keep_alive_time)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, keep_alive_interval)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_probes)


def _set_keepalive_windows(sock: socket.socket, keep_alive_time: int = 1, keep_alive_interval: int = 3, max_probes: int = 5):
    second = 1000

    struct_format = 'hh' if platform.system() == 'Windows' else 'ii'
    l_onoff = 0
    l_linger = 10
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_LINGER,
                    struct.pack(struct_format, l_onoff, l_linger))

    sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, keep_alive_time * second, keep_alive_interval * second))


def set_socket_keep_alive(
        sock: socket.socket,
        keep_alive_time: int = 10,
        keep_alive_interval: int = 3,
        max_probes: int = 10
):
    system = platform.system()

    if system == 'Windows':
        _set_keepalive_windows(sock, keep_alive_time, keep_alive_interval)
    elif system == 'Linux':
        _set_keepalive_linux(sock, keep_alive_time, keep_alive_interval, max_probes)

