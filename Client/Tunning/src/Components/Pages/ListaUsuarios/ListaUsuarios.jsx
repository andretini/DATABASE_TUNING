import axios from 'axios';
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export function ListaUsuarios() {
    const navigate = useNavigate();
    const [users, setUsers] = useState([]);
    const [error, setError] = useState(null);

    async function lista() {
        try {
            const response = await axios.get(
                'http://localhost:8000/users/all',
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    withCredentials: true,
                }
            );
            console.log('lista com sucesso:', response.data);
            return response.data;
            
        } catch (error) {
            console.error('Não:', error.response ? error.response.data : error.message);
            setError('Não funfou.');
            throw error;
        }
    }

    const handleDelete = async (userId) => {
        try {
            const response = await axios.delete(`http://localhost:8000/users/delete/${userId}`, {
                headers: {
                    'Content-Type': 'application/json',
                },
                withCredentials: true,
            });
            if (response.status === 200) {
                setUsers(users.filter(user => user.id !== userId));
            } else {
                throw new Error('Erro ao excluir usuário');
            }
        } catch (err) {
            setError('Erro ao excluir usuário');
            console.error(err);
        }
    };

    useEffect(() => {
        lista().then(data => setUsers(data)).catch(err => console.error(err));
    }, []);

    return (
        <div>
            <p style={{margin: '0 0 10px 50px'}}>Pagina Inicial:</p>
            {error && <p>{error}</p>}
            <ul>
                {users.map(user => (
                    <div key={user.id} style={{border: '2px dashed #575757', margin: '10px 0 10px 10px', padding: '10px'}}>
                        <li>Nome: {user.username}, Email: {user.email}</li>
                        <button 
                            style={{ backgroundColor: '#eb6960', color: 'white' , margin: '20px 0 20px'}}
                            onClick={() => handleDelete(user.id)}
                        >
                            Excluir
                        </button>
                    </div>
                ))}
            </ul>
        </div>
    );
}