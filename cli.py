"""CLI tool for code analysis"""
import click
from analyzer import CodeAnalyzer


@click.group()
def cli():
    """Code Analyzer - Analyze code files"""
    pass


@cli.command()
@click.argument("file_path", type=click.Path(exists=True))
def analyze(file_path):
    """Analyze a code file"""
    analyzer = CodeAnalyzer()
    result = analyzer.analyze_file(file_path)
    
    click.echo(f"📊 Analyzing: {file_path}\n")
    click.echo(f"Lines: {result.get('lines', 0)}")
    click.echo(f"Functions: {result.get('functions', 0)}")
    click.echo(f"Classes: {result.get('classes', 0)}")


@cli.command()
@click.argument("file_path", type=click.Path(exists=True))
def stats(file_path):
    """Get file statistics"""
    analyzer = CodeAnalyzer()
    result = analyzer.analyze_file(file_path)
    
    click.echo(f"📈 Statistics for: {file_path}\n")
    for key, value in result.items():
        click.echo(f"{key.capitalize()}: {value}")


if __name__ == "__main__":
    cli()
