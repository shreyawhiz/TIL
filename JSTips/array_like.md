# Array-like objects

Some objects look and smell like arrays, but aren't actually arrays:
```js
(function(){
	console.log(arguments.length); // 3
	console.log(arguments instanceof Array); // false
}(1, 2, 3));
```

Because these array-like objects aren't actually arrays, we can't iterate through them using `for in` syntax, nor can we call `forEach` on them. The good news though is that we can convert this to an array quite easily though using the `slice` function of the Array prototype:

```js
(function(){
	var argsArray = Array.prototype.slice.call(arguments);
	console.log(argsArray instanceof Array); // true
	argsArray.forEach(function (arg) {
		console.log(arg);
	});
	// 1
	// 2
	// 3
}(1, 2, 3));
```
