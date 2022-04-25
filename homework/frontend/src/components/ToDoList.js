import React from "react";


const ToDoItem = ({note}) => {
    return (
        <tr>
            <td>
                {note.id}
            </td>
            <td>
                {note.text}
            </td>
        </tr>
    )
}


const ToDosList = ({notes}) => {
    return (
        <table>
            <th>
                № Note
            </th>
            <th>
                Note name
            </th>

            {notes.map((note) => <ToDoItem note={note} /> )}
        </table>
    )
}


export default ToDosList