```javascript
var Model = new mongoose.Schema({
  email: {
    type: String,
    // This method holds the magic
    set: function(email) { 
      this._email = this.email;
      return email;
    }
});
```


Now you can access this._email, which contains the old value of email in your pre save hook.
