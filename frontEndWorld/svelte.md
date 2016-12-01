Frameworks without the framework
---------------------------------

"https://svelte.technology/blog/frameworks-without-the-framework/"

Svelte is a JS framework, which during our build process, complies HTML, CSS and JS code into standalone JavaScript modules.
Zip size being just 3.6 KB, its extremely light and FAST.

A small snippet from the article itself:

"Consider interoperability. Want to npm install cool-calendar-widget and use it in your app? Previously, you could only do that if you were already using (a correct version of) 
the framework that the widget was designed for – if cool-calendar-widget was built in React and you're using Angular then, well, hard cheese. But if the widget author used Svelte, 
apps that use it can be built using whatever technology you like. (On the TODO list: a way to convert Svelte components into web components.)"

"Or code splitting. It's a great idea (only load the code the user needs for the initial view, then get the rest later), but there's a problem 
– even if you only initially serve one React component instead of 100, you still have to serve React itself. With Svelte, code splitting can be much more effective, 
because the framework is embedded in the component, and the component is tiny."
