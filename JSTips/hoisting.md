# JavaScript Hoisting and Gotchas

Variables that are declared by the keyword `var` are "hoisted" to the top of the function scope. What does that mean though? Let's take a look:

```js
function log() {
  var value;
  console.log(value);
}

function log2() {
  console.log(value);
  var value;
}

log();
log2();
```

In the first function, the value is declared before we `console.log`. In the second function, the value is declared after. Should the second function throw an error?

The answer is no! The variable declaration of `value` is hoisted to the top of each function, no matter if it's written after a `console.log` or any other call, so both functions are identical and no error is thrown.

Where does this fail though?

```js
var value = 'outer';

function log3() {
  console.log(value);
  var value = 'inner';
}
log3();
```

What does this output? Is it 'outer', is it 'inner'? If you think either of those, then you've just learned something new, because it's actually `undefined`!

The reason for this is that in `log3`, **only the variable declaration** is hoisted to the top, **not the definition**. So value gets declared over the 'outer' one, but it doesn't get defined. Therefore, it just prints `undefined`.
