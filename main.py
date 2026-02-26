import click
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

# Initialize OpenAI client
client = OpenAI()
console = Console()

@click.command()
@click.argument('regex')
def regex_explain(regex):
    """AI-powered regular expression explainer."""
    console.print(f"[bold blue]Explaining regex: {regex}...[/bold blue]")

    prompt = f"""
    Provide a clear, human-readable explanation of the following regular expression.
    Regex: `{regex}`
    Format your response in Markdown.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {{"role": "system", "content": "You are an expert in regular expressions."}},
                {{"role": "user", "content": prompt}}
            ]
        )
        explanation_text = response.choices[0].message.content
        console.print(Markdown(explanation_text))
    except Exception as e:
        console.print(f"[bold red]Error during regex explanation:[/bold red] {e}")

if __name__ == '__main__':
    regex_explain()
