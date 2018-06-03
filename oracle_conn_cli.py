#!/usr/bin/env python
# -*- coding:utf-8 -*-

import signal
import getpass
import cx_Oracle
from plumbum import cli, colors
from plumbum.cli.application import T_


class OracleConnCLI(cli.Application):
    """
    An cli application to test oracle database connection through cx_Oracle.
    """
    
    AUTHOR = 'luoxu34'
    PROGNAME = colors.blue | 'OracleConnCLI'
    VERSION = colors.green | '0.01'

    _username = 'oracle'
    _password = ''
    _host = '127.0.0.1'
    _port = 1521
    _sid = 'orcl'
    
    @cli.switch('-u', str, help='login username of database')
    def set_login_username(self, username):
        self._username = username
    
    @cli.switch('-p', str, help='password of login user')
    def set_login_password(self, password):
        self._password = password

    @cli.switch(['-h', '--host'], str, 
                help='host ip or hostname where instance is running')
    def set_host_ip(self, ip):
        self._host = ip
 
    @cli.switch(['-P', '--port'], cli.Range(1, 65535), 
                help='listen port of instance, default 1521')
    def set_listener_port(self, port):
        self._port = port

    @cli.switch(['-s', '--sid'], str, help='instance name, default orcl')
    def set_sid(self, sid):
        self._sid = sid

    def main(self):
        if not self._password:
            self._password = getpass.getpass(
                'login username: {}\nlogin password: '.format(self._username))

        conn_str = '{}/{}@{}:{}/{}'.format(
            self._username, self._password, self._host, self._port, self._sid)
        print('connect string: {}'.format(conn_str))

        db = None
        try:
            db = cx_Oracle.connect(conn_str)
            msg = 'connect result: OK [sid: {}, version: {}]'.format(self._sid, db.version)
            print(colors.green | msg)
            return 0
        except Exception as exc:
            msg = 'connect result: failed [{}]'.format(exc)
            print(colors.red | msg)
            return 1
        finally:
            if db:
                db.close()

    @cli.switch(
        ['-v', '--version'], overridable=True, group='Meta-switches',
        help=T_('''Prints the program's version and quits'''))
    def version(self):
        print('{} {} by {}'.format(self.PROGNAME, self.VERSION, self.AUTHOR))


def user_exit(signum, frame):
    """ catch ctrl-c and exit program """
    print('\nstop progress, bye.\n')
    exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, user_exit)
    signal.signal(signal.SIGINT, user_exit)
    OracleConnCLI.run()
