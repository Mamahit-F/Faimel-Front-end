let people = ["Greg", "Mary", "Devon", "James"];
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
}

people.forEach(function (person) {
  console.log(person);
});
people.shift();
people.pop();
people.unshift("Matt");
people.push("Holy");
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
  if (people[i] === "Mary") {
    break;
  }
}
let copyOfPeople = people.slice(2);
people.splice(2, 1, "Elizabeth", "Artie");
let withBob = people.concat("Bob");
console.log("Final result with 'Bob':", withBob);
