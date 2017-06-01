# Virtuals
These are document properties that you can get and set but that do not get persisted to MongoDB. The getters are useful for formatting or combining fields, while setters are useful for de-composing a single value into multiple values for storage.

```javascript
// define a schema
var mediaSchema = new Schema({
  _source: {
    url: String,
    height: Number,
	width: Number
  }
});

// compile our model
var Medium = mongoose.model('Medium', mediaSchema);

// create a document
var imageSource = new Medium({
  _source: { url: 'Axl', height: 300, width: 150 }
});
```

Suppose you want 'source' field as a string url for legacy purposes. You could do it yourself:

```javascript
console.log(imageSource._source.url);
```

You will either create a parser on the fly or save a separate string field in the db.

A **virtual property getter** lets you define a source property that won't get persisted to MongoDB.

```javascript
mediaSchema.virtual('source').
	get(function() {
		return (this._source.url ? this._source.url : null);
	});
```

Now, mongoose will call your getter function every time you access the source property:

```javascript
console.log(imageSource.source);
```

mongoose will not include virtuals by default.
 Pass **{ virtuals: true }** to either toObject() or toJSON().
 
 
