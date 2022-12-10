import { useEffect, useState } from "react"
import { Wrapper } from "./Wrapper"

export const Products = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        (async () => {
            const response = await fetch('http://localhost:8000/products');
            const content = await response.json();
            setProducts(content);
        })();
    }, []);

    return <Wrapper>
    <div class="table-responsive">
        <table class="table table-striped table-sm">
            <thead>
                <tr>
                <th scope="col">ID</th>
                <th scope="col">Name</th>
                <th scope="col">Price</th>
                <th scope="col">Quantity</th>
                <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                {products.map(product => {
                    return <tr key={product.id}>
                        <td>{product.id}</td>
                        <td>{product.name}</td>
                        <td>{product.price}</td>
                        <td>{product.quantity}</td>
                        <td>
                            <a href="#" className="btn btn-sm btn-outline-secondary">
                                Delete
                            </a>
                        </td>
                    </tr>
                })}
            </tbody>
        </table>
  </div>
</Wrapper>
}