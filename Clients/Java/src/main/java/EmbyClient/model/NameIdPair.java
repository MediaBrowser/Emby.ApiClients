/*
 * Emby Server REST API
 * 
 */

package embyclient.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
/**
 * NameIdPair
 */


public class NameIdPair {
  @SerializedName("Name")
  private String name = null;

  @SerializedName("Id")
  private String id = null;

  public NameIdPair name(String name) {
    this.name = name;
    return this;
  }

   /**
   * The name.
   * @return name
  **/
  @Schema(description = "The name.")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public NameIdPair id(String id) {
    this.id = id;
    return this;
  }

   /**
   * The identifier.
   * @return id
  **/
  @Schema(description = "The identifier.")
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NameIdPair nameIdPair = (NameIdPair) o;
    return Objects.equals(this.name, nameIdPair.name) &&
        Objects.equals(this.id, nameIdPair.id);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, id);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NameIdPair {\n");
    
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
