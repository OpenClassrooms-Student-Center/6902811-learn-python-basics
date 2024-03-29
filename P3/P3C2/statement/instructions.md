# Instructions  

1. Use the `beautifulsoup4` module to **extract** the following information and **store** them in variables:

* To read the content of the file `index.html`, you must **copy-paste** the following code:

```
with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
```


* Retrieve the following elements in the HTML code and store them in variables:

```
- the page title (<title>)
- the text of the <h1> tag
- the names and prices of the products in the list (<ul>) (store them in a list)
- the descriptions of the products in the list (<ul>) (store them in a list).
```


2. **Display** the **extracted** information in the console.
3. **Convert** the prices from euro to dollars (consider that the price `dollar = euro * 1.2`).

#### Tips : 
* Don't forget to remove all unnecessary information (the word `price`, `:`, and the `€`) and convert the price to an integer using the `int()` function.
* Don't forget to add the `$` symbol after the converted price, for example: `20$`.

4. **Display** the new list with the `name` and the `new price in dollars`.
