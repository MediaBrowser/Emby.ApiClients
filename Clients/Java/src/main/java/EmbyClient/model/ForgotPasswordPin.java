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
 * ForgotPasswordPin
 */


public class ForgotPasswordPin {
  @SerializedName("Pin")
  private String pin = null;

  public ForgotPasswordPin pin(String pin) {
    this.pin = pin;
    return this;
  }

   /**
   * Get pin
   * @return pin
  **/
  @Schema(description = "")
  public String getPin() {
    return pin;
  }

  public void setPin(String pin) {
    this.pin = pin;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ForgotPasswordPin forgotPasswordPin = (ForgotPasswordPin) o;
    return Objects.equals(this.pin, forgotPasswordPin.pin);
  }

  @Override
  public int hashCode() {
    return Objects.hash(pin);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ForgotPasswordPin {\n");
    
    sb.append("    pin: ").append(toIndentedString(pin)).append("\n");
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
