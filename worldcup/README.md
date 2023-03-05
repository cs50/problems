# World Cup

Write a program to run simulations of the FIFA World Cup. 

```
$ python tournament.py 2018m.csv
Belgium: 20.9% chance of winning
Brazil: 20.3% chance of winning
Portugal: 14.5% chance of winning
Spain: 13.6% chance of winning
Switzerland: 10.5% chance of winning
Argentina: 6.5% chance of winning
England: 3.7% chance of winning
France: 3.3% chance of winning
Denmark: 2.2% chance of winning
Croatia: 2.0% chance of winning
Colombia: 1.8% chance of winning
Sweden: 0.5% chance of winning
Uruguay: 0.1% chance of winning
Mexico: 0.1% chance of winning
```

## Background

* In soccer, teams are given [FIFA Ratings](https://en.wikipedia.org/wiki/FIFA_World_Rankings#Current_calculation_method), which are numerical values representing the team's relative skill levels. Higher FIFA ratings indicate better previous game results, and we can determine the probability that a team wins a matchup if we have both teams' FIFA ratings via this formula: $P(W_1) = \dfrac{1}{10^{(-\frac{T_2-T_1}{600})} + 1}$ where $P(W_1)$ is the probability that Team 1 wins, $T1$ is the FIFA rating for Team 1, and $T2$ is the FIFA rating for Team 2.

* In the World Cup, 16 teams begin in the knockout round. At each round, half the teams are eliminated. When two teams remain, the winner of the final match is the champion and the loser is the runner-up. 

* The FIFA Ratings from just before the two previous World Cups are here: [May 2018 Men's FIFA Ratings](https://www.fifa.com/fifa-world-ranking/ranking-table/men/rank/id12189/) and [March 2019 Women's FIFA Ratings](https://www.fifa.com/fifa-world-ranking/ranking-table/women/rank/ranking_20190329/)
  

## Implementation Details

* Complete the implementation of `tournament.py` at right, such that it simulates a number of tournaments and outputs each team's probability of winning, for all probabilities greater than `0%`.

* In `main()`, your program should read in the file indicated by the user into the list `bracket`. This list should be a list of dictionaries, each dictionary containing `team` and `rating` keys, where the `rating` is of type `int`. 

  * Two files are provided: `2018m.csv` and `2019w.csv`. 

  * In each, the bracket of teams, in order, is provided along with their FIFA Ratings. 
    
    * Specifically, in the first round, the team in line 1 will play the team in line 2. The team in line 3 will play the team in line 4. Since there are 16 total lines, the first round will contain 8 total games. 

    * In the second round, the winner between lines 1 and 2 will play the winner between lines 3 and 4, etc.

    * The first few lines in `2018m.csv` look like this: 
    
    ```
      team,rating
      Uruguay,976
      Portugal,1306
      France,1166
    ```

* After, in `main()`, your program should simulate `N` tournaments, which, notice, has already been defined as `1000`. For each tournament, your program should return the winner and keep track of the number of wins for each team in the dictionary `counts`.

* In `simulate_tournament(bracket)`, your program should return the name of the winning team of one simulation of the given bracket. Your program should iterate through as many rounds as necessary to output one single winner of the tournament. 

* In `simulate_round(bracket)`, your program should simulate a single round of the tournament and return the winners of each game in that round.  
  
  * Note that in the first round, the first team should play the second, the third team should play the fourth, and so on. The results of the game should appear in order, where the winner between the first two teams appears before the winner of the next two teams in the resulting list. 

  * Additionally, for example, if the bracket given has 4 teams (third round), your program should simulate 2 games and return a list of the 2 winning teams. 

* Notice that `simulate_game(team1, team2)` has already been completed. Given two teams, it calculates the probability the first team defeats the second and returns `True` with that probability and `False` otherwise. We return `random.random() < probability` in this function, which is an application of Python's `random` module, where `random.random()` returns a pseudo-random value between 0 and 1. 


### Hints

* When reading in the file, you may find this syntax helpful, with `file_name` as the name of your file and `var` as a variable.

    ```python
    with open(file_name) as var:
        reader = csv.DictReader(var)
    ```

* Recall that a dictionary looks like this: `{'team': 'Uruguay', 'rating': 976}`. If this dictionary had variable name `example`, then `example["team"] = Uruguay` and `example["rating"] = 976`. 

* In Python, to add to a list, one can simply use the `.append()` function. 

* To check if a key, `k`, exists in a dictionary, `dict`, one can write a simple conditional: `if k in dict:`.

* Regarding helper functions, you may find the following helpful:
  * In `main()`, simulate the tournament `N` times with `simulate_tournament()`.
  * In `simulate_tournament()`, repeatedly simulate rounds until only `1` team remains with `simulate_round()`.
  * In `simulate_round()`, simulate each game in that round with `simulate_game()`.
  
### How to Test Your Code

Your program should behave per the examples below. Since simulations have randomness within each, your output will be different from the examples below. 

```
$ python tournament.py 2018m.csv
Belgium: 20.9% chance of winning
Brazil: 20.3% chance of winning
Portugal: 14.5% chance of winning
Spain: 13.6% chance of winning
Switzerland: 10.5% chance of winning
Argentina: 6.5% chance of winning
England: 3.7% chance of winning
France: 3.3% chance of winning
Denmark: 2.2% chance of winning
Croatia: 2.0% chance of winning
Colombia: 1.8% chance of winning
Sweden: 0.5% chance of winning
Uruguay: 0.1% chance of winning
Mexico: 0.1% chance of winning
```

```
$ python tournament.py 2019w.csv
Germany: 17.1% chance of winning
United States: 14.8% chance of winning
England: 14.0% chance of winning
France: 9.2% chance of winning
Canada: 8.5% chance of winning
Japan: 7.1% chance of winning
Australia: 6.8% chance of winning
Netherlands: 5.4% chance of winning
Sweden: 3.9% chance of winning
Italy: 3.0% chance of winning
Norway: 2.9% chance of winning
Brazil: 2.9% chance of winning
Spain: 2.2% chance of winning
China PR: 2.1% chance of winning
Nigeria: 0.1% chance of winning
```

* You might be wondering what actually happened at the 2018 and 2019 World Cups! For Men's, France won, defeating Croatia in the final. Belgium defeated England for the third place position. For Women's, the United States won, defeating the Netherlands in the final. England defeated Sweden for the third place position.

{% next %}

## How to Submit

TODO
