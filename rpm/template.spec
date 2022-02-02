%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-mavlink
Version:        2022.2.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mavlink package

License:        LGPLv3
URL:            https://mavlink.io/en/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-ros-workspace
BuildRequires:  cmake3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-future
BuildRequires:  python%{python3_pkgversion}-lxml
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ros-environment
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
MAVLink message marshaling library. This package provides C-headers and C++11
library for both 1.0 and 2.0 versions of protocol. For pymavlink use separate
install via rosdep (python-pymavlink).

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Feb 02 2022 Vladimir Ermakov <vooon341@gmail.com> - 2022.2.2-1
- Autogenerated by Bloom

* Wed Jan 05 2022 Vladimir Ermakov <vooon341@gmail.com> - 2022.1.5-1
- Autogenerated by Bloom

* Sun Dec 12 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.12.12-1
- Autogenerated by Bloom

* Thu Nov 11 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.11.11-1
- Autogenerated by Bloom

* Sun Oct 10 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.10.10-1
- Autogenerated by Bloom

* Thu Sep 09 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.9.9-1
- Autogenerated by Bloom

* Sun Jun 06 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.6.6-1
- Autogenerated by Bloom

* Wed May 05 2021 Vladimir Ermakov <vooon341@gmail.com> - 2021.5.5-1
- Autogenerated by Bloom

