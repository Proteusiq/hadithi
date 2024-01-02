use pyo3::prelude::*;
use crate::crab::KNN as rKNN;
use ndarray::Array1;

#[pyclass]
struct KNN {
    knn: rKNN,
}

#[pymethods]
impl KNN {
    #[new]
    fn new(k: usize) -> Self {
        KNN {
            knn: rKNN::new(k),
        }
    }

    fn fit(&mut self, x_train: Vec<Vec<f64>>, y_train: Vec<i32>) {
        let x_train: Vec<_> = x_train.into_iter().map(Array1::from).collect();
        self.knn.fit(x_train, y_train);
    }

    fn predict(&self, x_test: Vec<Vec<f64>>) -> Vec<i32> {
        let x_test: Vec<_> = x_test.into_iter().map(Array1::from).collect();
        self.knn.predict(x_test)
    }
}


#[pymodule]
fn knn(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<KNN>()?;
    Ok(())
}
