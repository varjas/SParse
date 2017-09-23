# SParse
## Installation
Clone the repository. Run the following command to install the bs4 dependency:
```
pip install bs4
```

## Usage
### CLI Script
Once installed, run the following command in the directory with the script:
```
python3 sparse/sparse.py
```

The program will prompt you for a full url, such as: `https://www.google.com`, and then for a list of filtering parameters. After filtering, the results can be saved as a .txt file.

### Module
The module can also be imported, and the `sparse` function used with a URL and filter parameters (both are `str` inputs):
```python
from sparse import sparse
sparse.sparse(url, parameters)
```
This function will return a `list` of data that is found.

## Filter Parameters
### Simple Filters
The filtering parameters can be any common identifier for html elements, with notation for different types of filters:

#### Class
Use the `.class` notation, for instance:
`.some-style` will find elements that have `class="some-style"`.

#### Tag
Use the `tag` notation, for instance:
`div` will find elements that use the `<div>` tag.

#### Attribute
Use the `[attribute]` notation, for instance:
`[data-id]` will find elements that have `data-id="someValue"`.

#### ID
Use the `#id` notation, for instance:
`#contents` will find the element that has `id="contents"`.

#### Return Values
Results are returned as a `list`. If the CLI script is used, results can be saved on separate lines in a .txt file.

By default, all text within the selected elements will be returned, including subelements.

If the `@` symbol is included after an attribute filter, the values for the attribute will be returned instead of text:
```
[data-id]@
```

### Combined Filters
Elements can be filtered with greater selectively by the combination of filter types without a space.

Elements can be filtered on multiple classes at the same time:
```
.bold.bright
```

Elements can be filtered by tag and attribute simultaneously:
```
h1[data-id]
```

### Sequenced Filters
Filters can be sequenced together if they are separated by a space. Later filters will only evaluate the results from the earlier filters.

The sequence below will filter for any element that has the `comment` class defined, and then find subelements that use the `h1` tag:
```
.comment h1
```

The sequence below will filter for any element that uses the `div` tag, and then find subelements with the `property` attribute defined:
```
div [property]
```

Elements found with the last filter will be used for data extraction.

### Advanced Filters
Additional notation for filters can be used to provide more specific selectivity. Other than usage of the `@` symbol in this package, all notation found in the [CSS selectors section](http://beautiful-soup-4.readthedocs.io/en/latest/#css-selectors) of the BeautifulSoup4 documentation should work.

The sequence below will filter for any element that uses the `div` tag, and then find direct sublements that use the `p` tag:
```
div > p
```

## License
Code released under the [MIT License](LICENSE.txt).

