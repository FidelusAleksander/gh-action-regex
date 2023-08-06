# Regex Validator Action

![Tests workflow](https://github.com/FidelusAleksander/gh-action-regex/actions/workflows/test.yaml/badge.svg)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/FidelusAleksander/gh-action-regex?logo=GitHub)](https://github.com/cicirello/Chips-n-Salsa/releases)


This action will check any text input against a regex pattern


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
        uses: FidelusAleksander/gh-action-regex@v0.3.0
        with:
          regex_pattern: "#[0-9]{5}"
          text: ${{ github.event.pull_request.title }}
```

### Using outputs
Check for a link anywhere inside Pull Request's description.
If not found, use official [github-script](https://github.com/marketplace/actions/github-script) action to post a comment in the PR
```yaml
- name: ADO WorkItem in description
  uses: FidelusAleksander/gh-action-regex@v0.3.0
  continue-on-error: true
  id: ado
  with:
    regex_pattern: "https://example.visualstudio.com/_apis/wit/workItems/[0-9]+"
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



### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `match`  | true if text matches the regex_pattern    |

### Debugging

Action will print in stdout a log in following format:
```json
{
    "regex_pattern": "#[0-9]{5}",
    "text": "#56570 Added test.py file",
    "match": true
}
```
