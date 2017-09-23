# SParse
A simple CLI tool and module to parse websites and extract specific information.

## Installation
Clone the repository. The parse script requires urllib and  bs4. Run the following command to install both packages:
```
pip install urllib bs4
```

## Usage
### Script
Once installed, run the following command in the directory with the script:
```
python3 sparse/sparse.py
```

The program will prompt you for a full url, such as: `https://www.google.com`, and then for a list of filtering parameters. After filtering, the results can be saved as a .txt file.

### Module
The module can also be imported:
```python
from sparse import sparse
```

And the `sparse` function used directly with a `str` URL and filter parameters:
```
sparse.sparse(url, parameters)
```

### Simple Filters
The filtering parameters can be any common identifier for html elements, with notation for different types of filters:

`.class` filters elements by a style class, such as:
	- `.title`
	- `.container`
	- `.default`
	- `.comment`
`tag` filters elements by tag, such as:
	- `div`
	- `a`
	- `h1`
	- `p`
`[attribute]` filters elements by attributes, such as:
	- `[href]`
	- `[property]`
	- `[data-id]`
	- `[role]`
`#id` filters elements by id, such as:
	- `#15315`
	- `#subtitle`
	- `#contents`
	- `#main`

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

