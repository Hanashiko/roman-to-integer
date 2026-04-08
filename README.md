# Roman to Integer

A Python script that converts Roman numeral strings to their integer equivalents.

## Usage

```bash
python main.py
```

By default, it converts `MCMXCIV` (1994) and prints the result.

## How it works

The function `romanToInteger` iterates through a Roman numeral string and applies the subtractive rule: if a smaller value appears before a larger one (e.g., `IV` = 4), it subtracts; otherwise, it adds.

## Supported symbols

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |
