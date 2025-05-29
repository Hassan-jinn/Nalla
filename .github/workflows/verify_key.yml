name: Verify Key
on:
  workflow_dispatch:
    inputs:
      key:
        description: 'Key to verify'
        required: true
jobs:
  verify_key:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests
      - name: Verify Key
        env:
          GITHUB_PAT: ${{ secrets.JINNPAT }}
          INPUT_KEY: ${{ github.event.inputs.key }}
        run: |
          python verify_key.py "$INPUT_KEY"
