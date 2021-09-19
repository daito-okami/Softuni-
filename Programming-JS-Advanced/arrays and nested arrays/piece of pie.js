function  pie(pies, startPie, endPie){
    const start = pies.indexOf(startPie)
    const  end = pies.indexOf(endPie)

    const result = pies.slice(start, end + 1)

    return result
}