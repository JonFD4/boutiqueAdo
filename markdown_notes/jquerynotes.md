# In product page
### Postload JavaScript Block

```html
{% block postloadjs %}
    {{ block.super }}
```
- `{% block postloadjs %}` starts a new block called `postloadjs`. This block will be placed in the corresponding block in the base template.
- `{{ block.super }}` ensures that any content defined in the parent template's `postloadjs` block is included here as well. This is useful if the parent template has some default JavaScript that you want to retain.

### Back to Top Link Click Event

```html
    <script type="text/javascript">
        $('.btt-link').click(function(e) {
            window.scrollTo(0,0)
        })
    </script>
```
- `<script type="text/javascript">` starts a script block with JavaScript.
- `$('.btt-link').click(function(e) { window.scrollTo(0,0) })` is a jQuery snippet:
    - `$('.btt-link')`: Selects all elements with the class `btt-link`.
    - `.click(function(e) { ... })`: Attaches a click event handler to these elements. When an element with the `btt-link` class is clicked:
    - `window.scrollTo(0,0)`: The window is scrolled to the top-left corner (coordinates 0,0).

### Sort Selector Change Event

```html
    <script type="text/javascript">
        $('#sort-selector').change(function() {
            var selector = $(this);
            var currentUrl = new URL(window.location);

            var selectedVal = selector.val();
            if(selectedVal != "reset"){
                var sort = selectedVal.split("_")[0];
                var direction = selectedVal.split("_")[1];

                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);

                window.location.replace(currentUrl);
            } else {
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");

                window.location.replace(currentUrl);
            }
        })
    </script>
```
- `<script type="text/javascript">` starts another script block with JavaScript.
- `$('#sort-selector').change(function() { ... })`: Uses jQuery to attach a change event handler to the element with the ID `sort-selector`. When the value of the sort selector changes:
    - `var selector = $(this);`: Stores the jQuery object for the sort selector in the variable `selector`.
    - `var currentUrl = new URL(window.location);`: Creates a `URL` object for the current page URL.
    - `var selectedVal = selector.val();`: Gets the selected value of the sort selector.
    - `if(selectedVal != "reset") { ... } else { ... }`: Checks if the selected value is not "reset".
        - If it's not "reset":
            - `var sort = selectedVal.split("_")[0];`: Splits the selected value by the underscore `_` and takes the first part as `sort`.
            - `var direction = selectedVal.split("_")[1];`: Splits the selected value by the underscore `_` and takes the second part as `direction`.
            - `currentUrl.searchParams.set("sort", sort);`: Sets the `sort` parameter in the URL's query string to the `sort` value.
            - `currentUrl.searchParams.set("direction", direction);`: Sets the `direction` parameter in the URL's query string to the `direction` value.
            - `window.location.replace(currentUrl);`: Redirects the browser to the updated URL.
        - If it is "reset":
            - `currentUrl.searchParams.delete("sort");`: Removes the `sort` parameter from the URL's query string.
            - `currentUrl.searchParams.delete("direction");`: Removes the `direction` parameter from the URL's query string.
            - `window.location.replace(currentUrl);`: Redirects the browser to the updated URL without the `sort` and `direction` parameters.

### Summary

1. **Scroll to Top**: When an element with the class `btt-link` is clicked, the window scrolls to the top.
2. **Sort Selector Change**: When the value of the sort selector changes, the script updates the URL with the selected sort and direction parameters, and reloads the page with the updated parameters. If "reset" is selected, it removes the sort and direction parameters from the URL.