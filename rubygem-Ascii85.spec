#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-Ascii85
Version  : 1.0.2
Release  : 11
URL      : https://rubygems.org/downloads/Ascii85-1.0.2.gem
Source0  : https://rubygems.org/downloads/Ascii85-1.0.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-Ascii85-bin
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
= Ascii85
* http://rubyforge.org/projects/ascii85
== Description
Ascii85 is a simple gem that provides methods for encoding/decoding Adobe's
binary-to-text encoding of the same name.

%package bin
Summary: bin components for the rubygem-Ascii85 package.
Group: Binaries

%description bin
bin components for the rubygem-Ascii85 package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n Ascii85-1.0.2
gem spec %{SOURCE0} -l --ruby > rubygem-Ascii85.gemspec

%build
gem build rubygem-Ascii85.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
Ascii85-1.0.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/Ascii85-1.0.2 && rake --trace test TESTOPTS="-v" && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/Ascii85-1.0.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/Ascii85.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/History.txt
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/bin/ascii85
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/lib/Ascii85/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/lib/ascii85.rb
/usr/lib64/ruby/gems/2.3.0/gems/Ascii85-1.0.2/spec/lib/ascii85_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/Ascii85-1.0.2.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/ascii85
