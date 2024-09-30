import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export function CreateAccountPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [error, setError] = useState(null);

    const navigate = useNavigate();

    async function criar(username, password, email, phone) {
        try {
            const response = await axios.post(
                'http://localhost:8000/users/create',
                { username, password, email, phone },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    withCredentials: true,  // Para incluir cookies
                }
            );
            console.log('Account Created:', response.data);
            navigate('/login')
            return response.data;
            
        } catch (error) {
            console.error('failed to create acoount:', error.response ? error.response.data : error.message);
            setError('Login failed. Please check your credentials.');
            throw error;
        }
    }

    const handleSubmit = async (e) => {
        e.preventDefault(); // Evita o reload da página
        setError(null); // Reseta o estado do erro

        try {
            await criar(username, password, email, phone);
            // Redirecionar ou fazer algo após o login bem-sucedido
        } catch (err) {
            // O erro já está sendo tratado na função `login`
        }
    };

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Username:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Phone:</label>
                    <input
                        type="text"
                        value={phone}
                        onChange={(e) => setPhone(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Cirar Conta</button>
            </form>

            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
}
