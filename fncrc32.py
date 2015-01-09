import zlib
import click

__version__ = "0.1alpha"


def crc32(file, chunk_size):
    checksum = None
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        if checksum:
            checksum = zlib.crc32(data, checksum) & 0xffffffff
        else:
            checksum = zlib.crc32(data) & 0xffffffff
    return checksum


@click.command()
@click.argument('files', type=click.File('rb', lazy=True), nargs=-1)
@click.option('--chunk-size', type=int, default=4096)
def main(files, chunk_size):
    for file in files:
        checksum = crc32(file, chunk_size)
        if not checksum:
            continue
        hex_checksum = "{0:08x}".format(checksum)
        message = ' [ {checksum} ] "{filename}"'.format(
            checksum=hex_checksum, filename=file.name)
        if hex_checksum in file.name.lower():
            message = click.style("".join((" ", message)), fg="green")
        else:
            message = click.style("".join(("!", message)), fg="red")
        click.echo(message)
