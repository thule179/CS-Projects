
var tiles = [];
var cells = [];
var empty_cell; // create a global variable for the empty cell

// establish solvable configurations, with 0 as the empty cell

var solvable_configs = [
  [6, 1, 10, 2, 7, 11, 4, 14, 5, 0, 9, 15, 8, 12, 13, 3],
  [10, 12, 7, 3, 5, 13, 8, 4, 9, 11, 2, 0, 15, 14, 1, 6],
  [6,1,7,5,2,9,8,4,15,11,12,13,14,3,0,10],
  [1,9,7,5,6,14,8,4,2,15,12,13,11,3,0,10],
  [10,15,7,5,13,12,8,4,6,2,11,1,14,0,3,9],
  [1,9,7,5,2,8,4,14,13,6,12,0,11,3,15,10],
  [9,7,5,4,1,2,0,8,13,6,12,14,11,3,15,10],
  [4,7,8,10,13,2,12,5,3,11,9,14,6,12,0,1],
  [11,14,12,8,13,6,5,10,9,1,7,2,3,0,15,4],
  [15,12,5,1,0,2,10,8,7,4,14,6,3,9,13,11],
];

var tile = document.getElementsByTagName("button");
var cell = document.getElementsByTagName("td");

// push cells into an array
for(var i = 0; i < cell.length; i++)
{
  cells.push(cell[i].id);
}

// push tiles into an array
for(var i = 0; i < tile.length; i++)
{
  tiles.push(tile[i].id);
}

random_idx = Math.floor(Math.random() * solvable_configs.length); // get solvable configurations at random

/* map tiles to solvable configs */
for (var i = 0; i < tiles.length; i++)
{
  if (solvable_configs[random_idx][i] == 0) // if meets empty cell in solvable config
  {
    // hide tile #0 in solvable config
    document.getElementById(tiles[i]).setAttribute("hidden", true);
    empty_cell = tiles[i]; // keep track of the empty cell
  }

  // display the tiles according to the solvable config
  document.getElementById(tiles[i]).innerHTML = solvable_configs[random_idx][i];
}

/* enable onclick() */
document.getElementById("1").onclick = swapButton;
document.getElementById("2").onclick = swapButton;
document.getElementById("3").onclick = swapButton;
document.getElementById("4").onclick = swapButton;
document.getElementById("5").onclick = swapButton;
document.getElementById("6").onclick = swapButton;
document.getElementById("7").onclick = swapButton;
document.getElementById("8").onclick = swapButton;
document.getElementById("9").onclick = swapButton;
document.getElementById("10").onclick = swapButton;
document.getElementById("11").onclick = swapButton;
document.getElementById("12").onclick = swapButton;
document.getElementById("13").onclick = swapButton;
document.getElementById("14").onclick = swapButton;
document.getElementById("15").onclick = swapButton;
document.getElementById("16").onclick = swapButton;

/* swap the tiles*/
function swapButton()
{
  /* grab the id of the button that was clicked */
  var caller_id = this.id;

  /* grab the cell of the button that was clicked */
  var caller_cell = tiles[tiles.indexOf(caller_id)];

  /* case: when the empty cell is on the right of the button that was clicked */
  var right_cell = tiles[tiles.indexOf(caller_id) + 1];
  
  if (right_cell != undefined && right_cell!=17 && document.getElementById(right_cell).innerHTML == 0 && caller_id != 4 && caller_id != 8 && caller_id != 12 && caller_id != 16)
  {
    document.getElementById(right_cell).removeAttribute("hidden");
    
    document.getElementById(right_cell).innerHTML = document.getElementById(caller_cell).innerHTML;
    
    document.getElementById(caller_cell).setAttribute("hidden",true);
    
    document.getElementById(caller_cell).innerHTML = 0;

    empty_cell = tiles[caller_cell];
  }

  
    /* case: when the empty cell is on the left of the button that was clicked */
  var left_cell = tiles[tiles.indexOf(caller_id) -1 ];
  
  if (left_cell != undefined && left_cell!=17 && document.getElementById(left_cell).innerHTML == 0 && caller_id != 1 && caller_id != 5 && caller_id != 9 && caller_id != 13 )
  {
    document.getElementById(left_cell).removeAttribute("hidden");
    
    document.getElementById(left_cell).innerHTML = document.getElementById(caller_cell).innerHTML;
    
    document.getElementById(caller_cell).setAttribute("hidden",true);
    
    document.getElementById(caller_cell).innerHTML = 0;

    empty_cell = tiles[caller_cell];
  }

   /* case: when the empty cell is on the top of the button that was clicked */
  var top_cell = tiles[tiles.indexOf(caller_id) - 4 ];
  
  if ( top_cell != undefined && document.getElementById(top_cell).innerHTML == 0 )
  {
    document.getElementById(top_cell).removeAttribute("hidden");
    
    document.getElementById(top_cell).innerHTML = document.getElementById(caller_cell).innerHTML;
    
    document.getElementById(caller_cell).setAttribute("hidden",true);
    
    document.getElementById(caller_cell).innerHTML = 0;

    empty_cell = tiles[caller_cell];
  }

   /* case: when the empty cell is under the button that was clicked */
  var bottom_cell = tiles[tiles.indexOf(caller_id) + 4 ];
  
  if (bottom_cell != undefined && document.getElementById(bottom_cell).innerHTML == 0 )
  {
    document.getElementById(bottom_cell).removeAttribute("hidden");
    
    document.getElementById(bottom_cell).innerHTML = document.getElementById(caller_cell).innerHTML;
    
    document.getElementById(caller_cell).setAttribute("hidden",true);
    
    document.getElementById(caller_cell).innerHTML = 0;

    empty_cell = tiles[caller_cell];
  }

}