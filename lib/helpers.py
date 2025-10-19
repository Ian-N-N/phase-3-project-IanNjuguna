def print_table(data, headers):
    """Print formatted data as a table."""
    col_widths = [max(len(str(row[i])) for row in data + [headers]) for i in range(len(headers))]
    print("\n" + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)))
    print("-" * (sum(col_widths) + len(headers) * 3))
    for row in data:
        print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(headers))))
    print()
