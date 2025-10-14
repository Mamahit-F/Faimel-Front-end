let programming = {
  languages: ["JavaScript", "Python", "Ruby"],
  isChallenging: true,
  isRewarding: true,
  difficulty: 8,
  jokes:
    "http://stackoverflow.com/questions/234075/what-is-your-best-programmer-joke",
};

programming.languages.push("Go");
console.log("Array languages setelah menambahkan 'Go':", programming.languages);

programming["difficulty"] = 7;
console.log(programming.difficulty);

delete programming.jokes;

programming.isFun = true;
console.log(programming);
console.log("\nArray languages setelah pemetaan:");
const formattedLanguages = programming.languages.map((language, index) => {
  return `${index} - ${language}`;
});
console.log(formattedLanguages);
