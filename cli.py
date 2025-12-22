"""CLI tool to check NeatCode backend features"""
import click
from backend import BackendClient


@click.group()
def cli():
    """Review Checker - Verify NeatCode backend"""
    pass


@cli.command()
def health():
    """Check backend health"""
    client = BackendClient()
    result = client.health_check()
    
    if result.get("healthy"):
        click.echo("✅ Backend is healthy")
    else:
        click.echo("❌ Backend is not healthy")
        if "error" in result:
            click.echo(f"   Error: {result['error']}")


@cli.command()
@click.option("--installation-id", required=True, help="GitHub installation ID")
@click.option("--owner", required=True, help="Repo owner")
@click.option("--repo", required=True, help="Repo name")
def check(installation_id, owner, repo):
    """Check if features are working"""
    client = BackendClient()
    
    # Check backend first
    health = client.health_check()
    if not health.get("healthy"):
        click.echo("❌ Backend is not healthy. Cannot check features.")
        return
    
    click.echo("✅ Backend is healthy")
    click.echo(f"\n📊 Checking features for {owner}/{repo}...")
    click.echo("\n⏳ Knowledge Graph: Not yet implemented")
    click.echo("⏳ Code Embeddings: Not yet implemented")
    click.echo("⏳ Grep Search: Not yet implemented")


if __name__ == "__main__":
    cli()

