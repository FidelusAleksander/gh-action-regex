# Regex Validator Action

This action will check Your input text against a regex pattern


### Example workflow
Check that the Pull Request title starts with a # followed by 5 numbers
```yaml
name: Your workflow
on:
  pull_request:
    types: [ opened, reopened, synchronize, edited]
    branches:
      - master

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Validate Title
        uses: FidelusAleksander/gh-action-regex@v0.2.0
        with:
          regex_pattern: "#[0-9]{5}"
          regex_match_type: match
          text: ${{ github.event.pull_request.title }}
```

### Using outputs
Check for a link anywhere inside Pull Request's description.
If not found, use official [github-script](https://github.com/marketplace/actions/github-script) action to post a comment in the PR
```yaml
- name: ADO WorkItem in description
  uses: FidelusAleksander/gh-action-regex@v0.2.0
  continue-on-error: true
  id: ado
  with:
    regex_pattern: "https://example.visualstudio.com/_apis/wit/workItems/[0-9]+"
    regex_match_type: search
    text: ${{ github.event.pull_request.body }}
- uses: actions/github-script@v5
  if: steps.ado.outputs.match == 'false'
  with:
    github-token: ${{secrets.GITHUB_TOKEN}}
    script: |
      github.rest.issues.createComment({
        issue_number: context.issue.number,
        owner: context.repo.owner,
        repo: context.repo.repo,
        body: '👋 Update the Description with link to ADO WorkItem!'
      })

```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `text`  | Text to evaluate    |
| `regex_pattern`  | Regex pattern to match the text against    |
| `regex_match_type` _(default=search)_  | Regex match type to use. One of [search, match, fullmatch]  [docs](https://docs.python.org/3/library/re.html)|


### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `match`  | true if text matches the regex_pattern    |

### Debugging

Action will print in stdout a log in following format:
```json
{
    "regex_match_type": "match",
    "regex_pattern": "#[0-9]{5}",
    "text": "#56570 Added test.py file",
    "match": true
}
```
