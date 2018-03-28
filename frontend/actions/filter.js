import {fetchStockData} from "../api/analisys";
export function changeStartDate(startDate) {
    return {
        type: 'CHANGE_START_DATE',
        startDate
    }
}

export function changeEndDate(endDate) {
    return {
        type: 'CHANGE_END_DATE',
        endDate
    }
}

export function changeCurrencyPair(pair) {
    return {
        type: 'CHANGE_CURRENCY_PAIR',
        pair
    }
}

export function changeFrequency(frequency) {
    return {
        type: 'CHANGE_FREQUENCY',
        frequency
    }
}

// todo develop it
export function loadStockDataFailure() {
    return {}
}

export function loadStockDataSuccess(stockData) {
    return {
        type: 'LOAD_STOCK_DATA_SUCCESS',
        stockData
    }
}
export function loadList() {
    return new Promise((resolve, reject) => {
        resolve(JSON.stringify(
            {}
        ))
    })
}
export function loadStockData() {

    return (dispatch) => {
        return fetchStockData()
            .then(stockData => {
                dispatch(loadStockDataSuccess(stockData))
            }).catch(error => {
                loadStockDataFailure(error)
            });
    };
}