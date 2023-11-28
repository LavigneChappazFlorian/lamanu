'use strict';

describe('Les nombres et opérations mathématiques : ', function () {
    it('Calculer la puissance d\'un nombre par rapport à un autre (x à la puissance y)', function () {
        var result = calculPuissance(2, 3);
        expect(result).toEqual(8);
    });
    it('Calculer la valeur absolue d\'un nombre', function () {
        var result = valeurAbsolue(-5);
        expect(result).toEqual(5);
    });
    it('Calculer les valeurs absolues d\'une liste de nombres', function () {
        var result = valeurAbsolueArray([-5,-50,-25,-568]);
        expect(result).toEqual([5,50,25,568]);
    });
    it('Calculer la surface d\'un cercle en fonction de son rayon. L\'arondir à l\'entier le plus proche', function () {
        var result = sufaceCercle(5);
        expect(result).toEqual(79);
    });
    it('Calculer l\'hypthènuse d\'un triangle rectangle', function () {
        var result = hypothenuse(5, 8);
        expect(result).toEqual(9.433981132056603);
    });
    it('Calculer l\'IMC (Poids / (taille x taille).Ne garder que deux chiffres après la virgule.', function () {
        var result = calculIMC(65, 1.75);
        expect(result).toEqual(21.22);
    });
})