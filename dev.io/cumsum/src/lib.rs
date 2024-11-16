
use pyo3::prelude::*;
use pyo3::wrap_pyfunction; // Required for wrapping functions

#[pyfunction]
fn cumsumx(data: Vec<i32>, max_reset: i32) -> Vec<i32> {
    data.iter()
        .scan(0, |total, &value| {
            *total += value;
            if *total > max_reset {
                *total = value;
            }
            Some(*total)
        })
        .collect()
}

#[pymodule]
fn cumsum(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(cumsumx, m)?)?;

    Ok(())
}
