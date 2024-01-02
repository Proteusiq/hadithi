use std::collections::HashMap;
use ndarray::Array1;

pub fn euclidean_distance(x1: &Array1<f64>, x2: &Array1<f64>) -> f64 {
    (x1 - x2).mapv(|a| a.powi(2)).sum().sqrt()
}

pub struct KNN {
    k: usize,
    x_train: Option<Vec<Array1<f64>>>,
    y_train: Option<Vec<i32>>,
}

impl KNN {
    pub fn new(k: usize) -> KNN {
        KNN { k, x_train: None, y_train: None }
    }

    pub fn fit(&mut self, x: Vec<Array1<f64>>, y: Vec<i32>) {
        self.x_train = Some(x);
        self.y_train = Some(y);
    }

    pub fn predict(&self, x: Vec<Array1<f64>>) -> Vec<i32> {
        x.iter().map(|xi| self.predict_one(xi)).collect()
    }

    fn predict_one(&self, x: &Array1<f64>) -> i32 {
        let x_train = self.x_train.as_ref().expect("Model not fitted");
        let y_train = self.y_train.as_ref().expect("Model not fitted");

        let distances = x_train.iter()
            .map(|x_train| euclidean_distance(x, x_train))
            .collect::<Vec<_>>();

        let mut indices: Vec<usize> = (0..distances.len()).collect();
        indices.sort_by(|&i, &j| distances[i].partial_cmp(&distances[j]).unwrap());

        let mut counter = HashMap::new();
        for &i in &indices[..self.k] {
            *counter.entry(y_train[i]).or_insert(0) += 1;
        }

        counter.into_iter()
            .max_by_key(|&(_, count)| count)
            .map(|(label, _)| label)
            .unwrap()
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_euclidean_distance() {
        let x1 = Array1::from(vec![1.0, 2.0]);
        let x2 = Array1::from(vec![4.0, 6.0]);
        let distance = euclidean_distance(&x1, &x2);
        let expected_distance = 5.0;
        assert!((distance - expected_distance).abs() < 1e-5);
    }

    #[test]
    fn test_knn_predict() {
        let mut knn = KNN::new(1);

        // Train the model with iris first and last data
        let x_train = vec![
            Array1::from(vec![5.1, 3.5, 1.4, 0.2]),
            Array1::from(vec![5.9, 3. , 5.1, 1.8]),
        ];
        let y_train = vec![0, 2];
        knn.fit(x_train, y_train);

        // Predict a known value iris second point
        let x_test = vec![Array1::from(vec![4.7, 3.2, 1.3, 0.2])];
        let predictions = knn.predict(x_test);

        assert_eq!(predictions, vec![0]);
    }
}