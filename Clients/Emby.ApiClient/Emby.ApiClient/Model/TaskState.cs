// <copyright file="TaskState.cs" company="Emby LLC">
// Emby.ApiClient. Autogenerated Code. No license applied. 
// </copyright>
// <autogenerated />
namespace Emby.ApiClient.Model
{
    using System;
    using System.Linq;
    using System.IO;
    using System.Text;
    using System.Collections;
    using System.Collections.Generic;
    using System.Collections.ObjectModel;
    using System.Runtime.Serialization;

    /// <summary>
    /// Enum TaskState  
    /// </summary>
    /// <value>Enum TaskState  </value>
    /// <seealso>MediaBrowser.Model.Tasks.TaskState</seealso>
    public enum TaskState
    {
        /// <summary>
        /// Enum Idle for value: Idle
        /// </summary>
        [EnumMember(Value = "Idle")]
        Idle = 1,
        /// <summary>
        /// Enum Cancelling for value: Cancelling
        /// </summary>
        [EnumMember(Value = "Cancelling")]
        Cancelling = 2,
        /// <summary>
        /// Enum Running for value: Running
        /// </summary>
        [EnumMember(Value = "Running")]
        Running = 3    }
}