# disclaimer: only works with Jupyter Notebook
from IPython.display import display, clear_output
bar = '▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊'
empty = '                                                  '
length = 1000
for i in range(length):
    clear_output(wait=True)
    prct = round(i/length * len(bar)/100) if round(i/length * (len(bar)/100) * 100 ) > 0 else 1
    display(f'{bar[:prct]} {empty[:-prct]}{round(i/length * 100)}%')