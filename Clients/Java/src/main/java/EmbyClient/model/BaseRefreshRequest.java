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
 * BaseRefreshRequest
 */


public class BaseRefreshRequest {
  @SerializedName("ReplaceThumbnailImages")
  private Boolean replaceThumbnailImages = null;

  public BaseRefreshRequest replaceThumbnailImages(Boolean replaceThumbnailImages) {
    this.replaceThumbnailImages = replaceThumbnailImages;
    return this;
  }

   /**
   * Get replaceThumbnailImages
   * @return replaceThumbnailImages
  **/
  @Schema(description = "")
  public Boolean isReplaceThumbnailImages() {
    return replaceThumbnailImages;
  }

  public void setReplaceThumbnailImages(Boolean replaceThumbnailImages) {
    this.replaceThumbnailImages = replaceThumbnailImages;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BaseRefreshRequest baseRefreshRequest = (BaseRefreshRequest) o;
    return Objects.equals(this.replaceThumbnailImages, baseRefreshRequest.replaceThumbnailImages);
  }

  @Override
  public int hashCode() {
    return Objects.hash(replaceThumbnailImages);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BaseRefreshRequest {\n");
    
    sb.append("    replaceThumbnailImages: ").append(toIndentedString(replaceThumbnailImages)).append("\n");
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
