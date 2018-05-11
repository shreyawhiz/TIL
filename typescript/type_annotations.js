var user = {
    firstName: "Tony",
    lastName: "Stark"
};
function sayHello(user) {
    console.log("Full Name added : " + user.firstName + " " + user.lastName);
}
;
sayHello(user);
/*
How to run a .ts file
1. install typescript -> npm install -g typescript
2. We now need to compile the ts file into a js file
3. Run typescript compiler in the cli -> tsc type_annotations.ts
4. will return a compiled .js file of the same name
5. Run the js file -> node type_annotations.js
6. OUTPUT -> Full Name added : Tony Stark
 */ 
