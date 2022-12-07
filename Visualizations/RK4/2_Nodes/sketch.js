// write a javascript function that adds two matrices together
// and returns the result
function addMatrices(m1, m2) {
    // create a new matrix to hold the result
    var result = [];
    // loop through the rows and columns of the matrices
    for (var i = 0; i < m1.length; i++) {
        for (var j = 0; j < m1[i].length; j++) {
            // add the values of the two matrices together
            result[i][j] = m1[i][j] + m2[i][j];
        }
    }
    // return the result
    return result;
}
