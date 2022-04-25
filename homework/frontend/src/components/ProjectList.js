import React from "react";


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                {project.name}
            </td>
        </tr>
    )
}


const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                № Project
            </th>
            <th>
                Project name
            </th>

            {projects.map((project) => <ProjectItem project={project} /> )}
        </table>
    )
}


export default ProjectList