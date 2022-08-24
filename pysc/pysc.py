#/usr/bin/env python3

import sys
import commands
import click

@click.group()
def cli():
    pass

@cli.command(help='Connect to the host')
# @click.argument('host', type=click.Choice(['rtc/i79dcgw1', '192.168.0.1', 'tele2/nin3-vsc1']))
@click.argument('host')
def connect():
    click.echo('Connecting to the host')
    
    commands.connect()

@cli.command()
def list():
    click.echo('Get list of hosts')

def main():
    cli()

    # if len(sys.argv) == 3:
    #     if sys.argv[1] == 'connect':
    #         commands.connect(sys.argv[2])

if __name__ == '__main__':
    main()