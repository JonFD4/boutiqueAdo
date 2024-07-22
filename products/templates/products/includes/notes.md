

### Increment and Decrement Quantity

#### 1. Increment Quantity
```javascript
$('.increment-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});
```

**Behavior:**
1. **Event Binding**: Attaches a click event handler to all elements with the class `increment-qty`.
2. **Prevent Default Action**: 
   ```javascript
   e.preventDefault();
   ```
   - Prevents the default behavior of the button (e.g., form submission or navigation).
3. **Find Closest Input**:
   ```javascript
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   ```
   - `$(this)`: Refers to the clicked button.
   - `.closest('.input-group')`: Traverses up the DOM to find the closest parent element with the class `input-group`.
   - `.find('.qty_input')[0]`: Searches for the input element with the class `qty_input` within the found `.input-group` and selects the first one.
4. **Get Current Value**:
   ```javascript
   var currentValue = parseInt($(closestInput).val());
   ```
   - Retrieves the current value of the quantity input and converts it to an integer.
5. **Increment Value**:
   ```javascript
   $(closestInput).val(currentValue + 1);
   ```
   - Increments the current value by 1 and updates the input field.
6. **Retrieve Item ID**:
   ```javascript
   var itemId = $(this).data('item_id');
   ```
   - Gets the `data-item_id` attribute from the clicked button to identify which item’s quantity is being changed.
7. **Update Button States**:
   ```javascript
   handleEnableDisable(itemId);
   ```
   - Calls the `handleEnableDisable` function to adjust the enable/disable state of the increment and decrement buttons based on the new quantity value.

#### 2. Decrement Quantity
```javascript
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});
```

**Behavior:**
1. **Event Binding**: Attaches a click event handler to all elements with the class `decrement-qty`.
2. **Prevent Default Action**:
   ```javascript
   e.preventDefault();
   ```
   - Prevents the default behavior of the button.
3. **Find Closest Input**:
   ```javascript
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   ```
   - Similar to the increment handler, this finds the closest quantity input within the `.input-group` that the button is a part of.
4. **Get Current Value**:
   ```javascript
   var currentValue = parseInt($(closestInput).val());
   ```
   - Retrieves the current value of the input field and converts it to an integer.
5. **Decrement Value**:
   ```javascript
   $(closestInput).val(currentValue - 1);
   ```
   - Decrements the current value by 1 and updates the input field.
6. **Retrieve Item ID**:
   ```javascript
   var itemId = $(this).data('item_id');
   ```
   - Gets the `data-item_id` attribute from the clicked button.
7. **Update Button States**:
   ```javascript
   handleEnableDisable(itemId);
   ```
   - Calls `handleEnableDisable` to update the button states based on the new quantity value.

### Handle Enable/Disable Function

#### `handleEnableDisable`
```javascript
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}
```

**Behavior:**
1. **Retrieve Current Value**:
   ```javascript
   var currentValue = parseInt($(`#id_qty_${itemId}`).val());
   ```
   - Uses the `itemId` to select the quantity input field (`#id_qty_${itemId}`) and get its value, converting it to an integer.
2. **Determine Disable States**:
   ```javascript
   var minusDisabled = currentValue < 2;
   var plusDisabled = currentValue > 98;
   ```
   - `minusDisabled`: Evaluates to `true` if the current value is less than 2, meaning the decrement button should be disabled.
   - `plusDisabled`: Evaluates to `true` if the current value is greater than 98, meaning the increment button should be disabled.
3. **Update Button States**:
   ```javascript
   $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
   $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
   ```
   - Uses `prop('disabled', ...)` to enable or disable the decrement and increment buttons based on the calculated states (`minusDisabled` and `plusDisabled`).

### Initialization on Page Load

#### Initialization Logic
```javascript
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}
```

**Behavior:**
1. **Select All Quantity Inputs**:
   ```javascript
   var allQtyInputs = $('.qty_input');
   ```
   - Selects all elements with the class `qty_input`.
2. **Loop Through Inputs**:
   ```javascript
   for(var i = 0; i < allQtyInputs.length; i++){
       var itemId = $(allQtyInputs[i]).data('item_id');
       handleEnableDisable(itemId);
   }
   ```
   - Loops through each quantity input element.
   - Retrieves the `item_id` from the `data-item_id` attribute of each input.
   - Calls `handleEnableDisable` for each `item_id` to ensure that the buttons are enabled or disabled correctly when the page loads.

### Update Enable/Disable State on Input Change

#### Input Change Handler
```javascript
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});
```

**Behavior:**
1. **Event Binding**:
   ```javascript
   $('.qty_input').change(function() {
   ```
   - Attaches a change event handler to all quantity input elements.
2. **Retrieve Item ID**:
   ```javascript
   var itemId = $(this).data('item_id');
   ```
   - Gets the `data-item_id` attribute from the changed input element.
3. **Update Button States**:
   ```javascript
   handleEnableDisable(itemId);
   ```
   - Calls `handleEnableDisable` to update the enable/disable states of the increment and decrement buttons based on the new value of the input.

### Summary

- **Increment/Decrement Handlers**: Modify the quantity in the input field and update the button states accordingly.
- **Handle Enable/Disable Function**: Adjusts the enable/disable state of the increment and decrement buttons based on the current quantity.
- **Initialization**: Ensures that the buttons are correctly enabled or disabled when the page loads.
- **Input Change Handler**: Updates the button states whenever the user manually changes the quantity.

This script ensures a smooth user experience by keeping the increment and decrement buttons enabled or disabled based on the quantity value and by reflecting any changes immediately.