Short-circuits conditionals
---------------------------

If you have to execute a function just if a condition is true, like this:

if(condition){
    dosomething();
}

You can use a short-circuit just like this:

	condition && dosomething();



	LINK: http://www.jstips.co/en/three-useful-hacks/