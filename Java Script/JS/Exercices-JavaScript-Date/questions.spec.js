'use strict';

describe('Les dates : ', function () {

    it('Extraire l`\année à quatre chiffre de la date', function () {
        var date = new Date('2018-10-01');
        var result = getYear(date);
        expect(result).toEqual(2018);
    });
    
    it('Extraire le mois de la date', function () {
        var date = new Date('2018-10-01');
        var result = getMonth(date);
        expect(result).toEqual(9);
    });

    it('Extraire le jour du mois de la date', function () {
        var date = new Date('2018-10-01');
        var result = getDayOfTheMonth(date);
        expect(result).toEqual(1);
    });
    
    it('Extraire le jour de la semaine de la date', function () {
        var date = new Date('2018-10-01');
        var result = getTheWeekDay(date);
        expect(result).toEqual(1);
    });

    it('Remplacer l\'année de la date par 2020', function () {
        var date = new Date('2018-10-01');
        var result = modifyYear(date);
        expect(result.getFullYear()).toEqual(2020);
    });    
    it('Mettre la date au format ISO', function () {
        var date = new Date('2018-10-01');
        var result = convertDateToISOFormat(date);
        expect(result).toEqual("2018-10-01T00:00:00.000Z");
    });    
    it('Mettre la date au format local jj/mm/YYYY', function () {
        var date = new Date('2018-10-01');
        var result = convertDateToLocalFormat(date);
        expect(result).toEqual("01/10/2018");
    });    
    it('Récupérer la date courante', function () {
        var date = new Date();
        var result = getCurrentDate();
        expect(result).toEqual(date);
    });    
    it('Convertir la date au format long texte en français "ex: jeudi 1 octobre 2020"', function () {
        var date = new Date(Date.UTC(2020,8,27));
        var result = getCurrentLocalDateString(date);
        expect(result).toEqual('dimanche 27 septembre 2020');
    });    
});