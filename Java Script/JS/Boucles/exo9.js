let grid=" ";

for (let line=0; line<8;line++){

    for (let col = 0; col<8; col++){
        grid+=(line+col)%2?'#':' ';
    }
    grid+="\n";
}

console.log(grid);