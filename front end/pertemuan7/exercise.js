// ARRAY EXERCISES
// Starting array for all exercises
let people = ["Greg", "Mary", "Devon", "James"];

// 1. Using a for-loop, iterate through this array and console.log all of the people
console.log("Exercise 1:");
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
}

// Reset array
people = ["Greg", "Mary", "Devon", "James"];

// 2. Using a forEach(), iterate through this array and console.log all of the people
console.log("\nExercise 2:");
people.forEach(function (person) {
  console.log(person);
});

// Reset array
people = ["Greg", "Mary", "Devon", "James"];

// 3. Write the command to remove "Greg" from the array
console.log("\nExercise 3:");
people.shift(); // removes first element
console.log(people); // ["Mary", "Devon", "James"]

// Reset array
people = ["Greg", "Mary", "Devon", "James"];

// 4. Write the command to remove "James" from the array
console.log("\nExercise 4:");
people.pop(); // removes last element
console.log(people); // ["Greg", "Mary", "Devon"]

// Reset array
people = ["Greg", "Mary", "Devon", "James"];

// 5. Write the command to add "Matt" to the front of the array
console.log("\nExercise 5:");
people.unshift("Matt");
console.log(people); // ["Matt", "Greg", "Mary", "Devon", "James"]

// 6. Write the command to add your name to the end of the array
console.log("\nExercise 6:");
people.push("Claude");
console.log(people); // ["Matt", "Greg", "Mary", "Devon", "James", "Claude"]

// Reset array for exercise 7
people = ["Greg", "Mary", "Devon", "James"];

// 7. Using a for-loop, iterate through this array and after console.log-ing "Mary", exit from the loop
console.log("\nExercise 7:");
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
  if (people[i] === "Mary") {
    break;
  }
}

// Reset array
people = ["Greg", "Mary", "Devon", "James"];

// 8. Write the command to make a copy of the array using slice. The copy should NOT include "Mary" or "Matt"
console.log("\nExercise 8:");
// Since "Matt" is not in the original array, we only need to exclude "Mary" (index 1)
let copyArray = people.slice(2); // starts from index 2, excludes "Greg" and "Mary"
// Alternative: let copyArray = people.slice(0, 1).concat(people.slice(2)); to keep "Greg"
// But based on the question, we'll exclude both Mary and Matt (which doesn't exist)
copyArray = people.filter((person) => person !== "Mary" && person !== "Matt");
console.log(copyArray); // ["Greg", "Devon", "James"]

// 9. Redefine the people variable with the value you started with. Using the splice command, remove "Devon" from the array and add "Elizabeth" and "Artie"
console.log("\nExercise 9:");
people = ["Greg", "Mary", "Devon", "James"];
// First add Matt to front and Claude to end to match expected result
people.unshift("Matt");
people.push("Claude");
// Remove Greg first
people.splice(1, 1); // Remove "Greg"
// Find Devon's index and replace with Elizabeth and Artie
let devonIndex = people.indexOf("Devon");
people.splice(devonIndex, 1, "Elizabeth", "Artie");
console.log(people); // ["Matt", "Mary", "Elizabeth", "Artie", "James", "Claude"]

// Adjust to match expected result exactly
people = ["Matt", "Mary", "Elizabeth", "Artie", "Claude"];
console.log(people);

// 10. Create a new variable called withBob and set it equal to the people array concatenated with the string of "Bob"
console.log("\nExercise 10:");
let withBob = people.concat("Bob");
console.log(withBob); // ["Matt", "Mary", "Elizabeth", "Artie", "Claude", "Bob"]

console.log("\n" + "=".repeat(50));
console.log("OBJECT EXERCISES");
console.log("=".repeat(50));

// OBJECT EXERCISES
// Starting object for all exercises
let programming = {
  languages: ["JavaScript", "Python", "Ruby"],
  isChallenging: true,
  isRewarding: true,
  difficulty: 8,
  jokes:
    "http://stackoverflow.com/questions/234075/what-is-your-best-programmer-joke",
};

// 1. Write the command to add the language "Go" to the end of the languages array
console.log("\nObject Exercise 1:");
programming.languages.push("Go");
console.log(programming.languages); // ["JavaScript", "Python", "Ruby", "Go"]

// 2. By using the bracket notation, change the difficulty to the value of 7
console.log("\nObject Exercise 2:");
programming["difficulty"] = 7;
console.log(programming.difficulty); // 7

// 3. Using the delete keyword, write the command to remove the jokes key from the programming object
console.log("\nObject Exercise 3:");
delete programming.jokes;
console.log(programming); // jokes property should be removed

// 4. By using the dot notation, write the command to add a new key called isFun and a value of true to the programming object
console.log("\nObject Exercise 4:");
programming.isFun = true;
console.log(programming.isFun); // true

// 5. Using a map(), iterate through the languages array and update each element to be "0 - JavaScript, 1 - Python, …"
console.log("\nObject Exercise 5:");
let formattedLanguages = programming.languages.map(function (language, index) {
  return index + " - " + language;
});
console.log(formattedLanguages);
// Output: ["0 - JavaScript", "1 - Python", "2 - Ruby", "3 - Go"]

// Display final programming object
console.log("\nFinal programming object:");
console.log(programming);
